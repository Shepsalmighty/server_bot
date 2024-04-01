import boto3
from botocore.exceptions import ClientError
import logging
import time
import datetime
from datetime import datetime as dt



logger = logging.getLogger(__name__)

class ServerControls:

    def __init__(self, ec2_resource, instance=None):
        self.ec2_resource = ec2_resource
        self.instance = instance
        self.start_time = dt.time(8,0)
        self.end_time = dt.time(18,0)

    @classmethod
    def from_resource(cls):
        ec2_resource = boto3.resource("ec2")
        return cls(ec2_resource)


    def serverCreate(self,image, instance_type, key_pair, security_groups=None):
        """
               Creates a new EC2 instance. The instance starts immediately after
               it is created.

               The instance is created in the default VPC of the current account.

               :param image: A Boto3 Image object that represents an Amazon Machine Image (AMI)
                             that defines attributes of the instance that is created. The AMI
                             defines things like the kind of operating system and the type of
                             storage used by the instance.
               :param instance_type: The type of instance to create, such as 't2.micro'.
                                     The instance type defines things like the number of CPUs and
                                     the amount of memory.
               :param key_pair: A Boto3 KeyPair or KeyPairInfo object that represents the key
                                pair that is used to secure connections to the instance.
               :param security_groups: A list of Boto3 SecurityGroup objects that represents the
                                       security groups that are used to grant access to the
                                       instance. When no security groups are specified, the
                                       default security group of the VPC is used.
               :return: A Boto3 Instance object that represents the newly created instance.
               """
        try:
            instance_params = {
                "ImageId": image.id,
                "InstanceType": instance_type,
                "KeyName": key_pair.name,
            }
            if security_groups is not None:
                instance_params["SecurityGroupIds"] = [sg.id for sg in security_groups]
            self.instance = self.ec2_resource.create_instances(
                **instance_params, MinCount=1, MaxCount=1
            )[0]
            self.instance.wait_until_running()
        except ClientError as err:
            logging.error(
                "Couldn't create instance with image %s, instance type %s, and key %s. "
                "Here's why: %s: %s",
                image.id,
                instance_type,
                key_pair.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return self.instance

    def serverDel(self):
        """
                Terminates an instance and waits for it to be in a terminated state.
                """
        if self.instance is None:
            logger.info("No instance to terminate.")
            return

        instance_id = self.instance.id
        try:
            self.instance.terminate()
            self.instance.wait_until_terminated()
            self.instance = None
        except ClientError as err:
            logging.error(
                "Couldn't terminate instance %s, due to: %s: %s",
                instance_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
    def serverUp(self):

        if self.instance is None:
            logger.info("No instance to start.")
            return

        try:
            response = self.instance.start()
            self.instance.wait_until_running()
        except ClientError as err:
            logger.error(
                "Couldn't start instance %s, due to: %s: %s",
                self.instance.id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response



    def serverDown(self):

        if self.instance is None:
            logger.info("No instance to stop.")
            return

        try:
            response = self.instance.stop()
            self.instance.wait_until_stopped()
        except ClientError as err:
            logger.error(
                "Couldn't stop instance %s, due to: %s: %s",
                self.instance.id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response

    def serverExtend(self, param):
        extend = (dt.combine(dt.now().date(), self.end_time) + datetime.timedelta(hours= param)).time()

        return extend




    # automate servers coming online, weekdays between 8am and 6pm
    def serverAuto(self, current_time):
        weekday = current_time.weekday()
        is_weekday = weekday >= 0 and weekday <= 4

        in_work_hours = self.start_time <= current_time < self.end_time

        if is_weekday and in_work_hours and self.instance:
            ServerControls.serverUp(self)
            print("Servers coming online")
        elif not is_weekday and not in_work_hours and self.instance and not self.serverExtend:
            ServerControls.serverDown(self)


now = ServerControls.serverAuto(self, current_time)


if __name__ == '__main__':
    ServerControls.serverAuto()