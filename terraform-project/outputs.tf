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

output "private_key_pem" {
  description = "Private key to connect to the EC2 instance. Store this securely."
  value       = tls_private_key.deployer_key.private_key_pem
  sensitive   = true
}