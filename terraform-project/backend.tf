terraform {
  backend "s3" {
    bucket         = "souvroy20-terraform-state-2025"
    key            = "python-devops/mystatefile/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock-souvroy20"
    encrypt        = true
  }
}