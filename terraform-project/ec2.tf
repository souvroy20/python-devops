resource "aws_key_pair" "deployer" {
  key_name   = "terra-automate-key"
public_key = file("C:\\IMPORTANT\\AWS_Keys\\terraform_python.pub")
}

resource "aws_default_vpc" "default" {

}

resource "aws_security_group" "allow_user_to_connect" {
  name        = "allow TLS"
  description = "Allow user to connect"
  vpc_id      = aws_default_vpc.default.id
  ingress {
    description = "port 22 allow"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = " allow all outgoing traffic "
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "port 80 allow"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "port 443 allow"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "mysecurity"
  }
}

data "aws_iam_instance_profile" "existing" {
  name = "Github-Action-Terraform-Automation"
}

resource "aws_instance" "testinstance" {
  ami             = var.ami_id
  instance_type   = var.instance_type
  iam_instance_profile   = data.aws_iam_instance_profile.existing.name
  key_name        = aws_key_pair.deployer.key_name
  ebs_optimized   = true
  security_groups = [aws_security_group.allow_user_to_connect.name]
  user_data = <<-EOF
              #!/bin/bash
              exec > /var/log/user-data.log 2>&1
              set -x
              apt update -y
              apt install -y apache2
              systemctl start apache2
              systemctl enable apache2
              echo "<html><body><h1>EC2 Instance is working!</h1></body></html>" > /var/www/html/index.html
              EOF
  tags = {
    Name = "Automate Python Terraform"
  }
  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }
}
