output "instance_ip" {
  value = aws_instance.testinstance.public_ip
}

output "instance_id" {
  value = aws_instance.testinstance.id
}

output "instance_type" {
  value = aws_instance.testinstance.instance_type
}
output "instance_private_ip" {
  value = aws_instance.testinstance.private_ip
}

output "public_key" {
  value = aws_key_pair.deployer.public_key
}