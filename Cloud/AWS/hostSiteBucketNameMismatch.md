# 🌐 Hosting a Static Website with S3 (Non-Matching Bucket Name), CloudFront & Route 53 (HTTPS)

## 🧾 Prerequisites

- An AWS account
- A registered domain (e.g., `example.com`)
- Static website files (`index.html`, `error.html`, etc.)

---

## 🔧 Step 1: Create an S3 Bucket (Name Doesn't Have to Match Domain)

1. Go to the **S3 Console**
2. Create a bucket with any unique name, e.g., `my-static-site-bucket`
3. **Block all public access**
4. Upload your static website files
5. (Optional) If you want to test directly with the S3 website endpoint:
   - Enable **Static Website Hosting**
   - Index document: `index.html`
   - Error document: `error.html`

> ⚠️ **Note**: Static website endpoints (e.g., `s3-website-region.amazonaws.com`) don't support HTTPS. We will use CloudFront for HTTPS support.

---

## 🔒 Step 2: Request an SSL Certificate (ACM)

1. Go to **AWS Certificate Manager** in **us-east-1 (N. Virginia)**
2. Request a **Public Certificate** for:
   - `example.com`
   - `www.example.com` (optional)
3. Use **DNS validation**
4. Add the provided **CNAME record** in **Route 53 > Hosted Zones**
5. Wait for the certificate status to become **Issued**

---

## 🚀 Step 3: Create a CloudFront Distribution

1. Go to **CloudFront > Create Distribution**
2. **Origin domain**:
   - Set to the **REST endpoint** of your bucket: `my-static-site-bucket.s3.amazonaws.com`
3. Enable **Origin Access Control (OAC)** or **Origin Access Identity (OAI)**:
   - This ensures CloudFront can access private content
   - You’ll need to grant read permissions to CloudFront in the S3 bucket policy
4. Set **Viewer Protocol Policy** to:
   - `Redirect HTTP to HTTPS`
5. Add **Alternate Domain Names (CNAMEs)**:
   - `example.com`
   - `www.example.com` (optional)
6. Choose your **SSL Certificate** from ACM
7. Set **Default Root Object** to `index.html`
8. Click **Create Distribution**
9. Wait for deployment (~15 minutes)

---

## 🌍 Step 4: Configure Route 53 DNS Records

1. Go to **Route 53 > Hosted Zones > your domain**
2. Create an **A Record**:
   - Name: `example.com`
   - Type: `A – IPv4 address`
   - Alias: **Yes**
   - Alias Target: **CloudFront distribution domain name** (e.g., `d123abcd.cloudfront.net`)
3. _(Optional)_ Redirect `www` to non-www:
   - Create an S3 bucket: `www.example.com`
   - Enable static website hosting with redirection
   - Add a CloudFront distribution for it
   - Point `www.example.com` to that CloudFront distribution in Route 53

---

## ✅ Step 5: Test Your Website

- Open `https://example.com` in your browser
- You should see your site securely served via CloudFront

---

## 🔐 Security & Best Practices

- Use **OAC or OAI** instead of public S3 access
- Block all public access to your S3 bucket
- Enable **CloudFront logging** for observability
- Set **cache-control headers** for asset caching
- Use **WAF (Web Application Firewall)** for protection

---

## 🛠 Optional Enhancements

- Automate setup with **Terraform** or **AWS CDK**
- Add custom error pages (e.g., 404.html)
- Deploy via CI/CD pipelines

---
