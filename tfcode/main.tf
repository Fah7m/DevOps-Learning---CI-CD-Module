provider "aws"{
region="us-east-1"
}

# Intentionally poor formatting + bad practices
resource "aws_s3_bucket" "ExampleBucket" {
bucket = "MyExampleBucket123"
acl="public-read"

tags ={
  Name= "My Example Bucket"
  Environment="Dev"
  owner = "admin"
}
}

# Missing required variable reference (aws_region unused)
resource "aws_instance" "web"{
ami = "ami-0c55b159cbfafe1f0"
instance_type = "t2.micro"
  tags = {
  Name = "WebServer"
}
}
