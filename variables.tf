variable "aws_region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "compliance-pipeline"
}

variable "github_repo" {
  description = "GitHub repo in format owner/repo-name"
}

variable "github_branch" {
  default = "main"
}

variable "github_token_secret" {
  description = "AWS Secrets Manager secret name storing the GitHub OAuth token"
}
