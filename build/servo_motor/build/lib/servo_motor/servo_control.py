import rclpy
from rclpy.node import Node
import serial

class ServoControl(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.serial = serial.Serial('/dev/ttyUSB0', 9600)
        self.timer = self.create_timer(1.0, self.move_servo)

    def move_servo(self):
        self.angle += 10
        if self.angle > 180:
            self.angle = 0
        cmd = f"{self.angle}\n"
        self.serial.write(cmd.encode())
        self.get_logger().info(f'Enviado: {self.angle}')


def main(args=None):
    rclpy.init(args=args)
    servo_control = ServoControl()
    rclpy.spin(servo_control)
    rclpy.shutdown()

if __name__ == '__main__':
    main()