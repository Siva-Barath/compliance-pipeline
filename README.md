# Automated Compliance Scans for Containerized Applications
## AWS CodeBuild + AWS CodePipeline

## Architecture

```
GitHub → CodePipeline → [Build] → [Compliance Scan] → [Deploy to ECS Fargate]
                          ↓               ↓
                         ECR         Trivy + Checkov
                                     (blocks deploy
                                      on HIGH/CRITICAL)
```

## Compliance Scans

| Tool     | What it scans                          | Fails pipeline on        |
|----------|----------------------------------------|--------------------------|
| Trivy    | Container image CVEs                   | HIGH or CRITICAL severity |
| Checkov  | Terraform IaC misconfigurations        | HIGH severity (soft-fail on MEDIUM) |
| ECR Scan | AWS-native image scanning on push      | Informational only       |

## Prerequisites

- AWS CLI configured
- Terraform >= 1.5
- GitHub repository with this code
- GitHub OAuth token stored in AWS Secrets Manager

## Setup

### 1. Store GitHub token in Secrets Manager
```bash
aws secretsmanager create-secret \
  --name github-oauth-token \
  --secret-string "YOUR_GITHUB_TOKEN"
```

### 2. Deploy infrastructure
```bash
terraform init

terraform apply \
  -var="github_repo=your-org/your-repo" \
  -var="github_token_secret=github-oauth-token"
```

### 3. Push code to trigger pipeline
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

## Pipeline Stages

1. Source — pulls code from GitHub on every push to `main`
2. Build — builds Docker image, pushes to ECR
3. ComplianceScan — runs Trivy + Checkov; **blocks deploy if HIGH/CRITICAL CVEs found**
4. Deploy — updates ECS Fargate service with new image (only if scan passes)

## Scan Reports

Compliance reports are stored as CodeBuild artifacts in S3:
- `trivy-report.json` — container vulnerability report
- `checkov-report.json` — IaC misconfiguration report

View them in the CodeBuild console under **Reports**.
