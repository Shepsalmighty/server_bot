import boto3
import time
import datetime


class ServerControls:

    def __init__(self, ec2_resource, instance=None):
        self.ec2_resource = ec2_resource
        self.instance = instance

    @classmethod
    def from_resource(cls):
        ec2_resource = boto3.resource("ec2")
        return cls(ec2_resource)


    def serverCreate(self):
        pass

    def serverDel(self):
        pass
    def serverUp(self):
        pass

    def serverDown(self):
        pass

    def serverExtend(self):
        pass

    # automate servers coming online, weekdays between 8am and 6pm
    def serverAuto(self, current_time):
        start_time = datetime(current_time.year, current_time.month, current_time.day, 8, 0)
        end_time = datetime(current_time.year, current_time.month, current_time.day, 18, 0)

        weekday = current_time.weekday()
        is_weekday = weekday >= 0 and weekday <= 4

        in_work_hours = current_time >= start_time and current_time < end_time

        if is_weekday and in_work_hours and self.instance is None:
            ServerControls.serverUp()
            print("Servers coming online")
        elif not is_weekday and not in_work_hours and self.instance is not None:
            ServerControls.serverDown()


now =
ServerControls.serverAuto(self, current_time)


if __name__ == '__main__':
    ServerControls.serverAuto()