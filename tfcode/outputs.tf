output "bucket_name" {
value = aws_s3_bucket.ExampleBucket.bucket
description="Outputs bucket name"
}

output "server_id" {
value= aws_instance.web.id
}
