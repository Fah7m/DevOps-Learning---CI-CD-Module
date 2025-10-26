variable "aws_region" {
type = string
default = "us-east-1"
}

# Unused variable to trigger lint warning
variable "instance_name" {
  description = "Name of the EC2 instance"
  type = string
  default = "MyServer"
}
