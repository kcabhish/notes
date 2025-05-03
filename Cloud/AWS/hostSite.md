# 🌐 Hosting a Static Website with S3, Route 53, and CloudFront (HTTPS Enabled)

## 🧾 Prerequisites

- An AWS account
- A registered domain (e.g., `example.com`)
- Static website files (`index.html`, `error.html`, etc.)

---

## 🔧 Step 1: Create and Configure the S3 Bucket

1. Go to the **S3 Console**
2. Create a bucket named **exactly** like your domain (e.g., `example.com`)
3. **Uncheck** "Block all public access"
4. Upload your static website files
5. Enable **Static Website Hosting**:
   - Index document: `index.html`
   - Error document: `error.html` (optional)
6. Note your website endpoint (e.g., `http://example.com.s3-website-us-east-1.amazonaws.com`)

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
2. Set **Origin domain** to the **S3 website endpoint**
3. Set **Viewer Protocol Policy** to:
   - `Redirect HTTP to HTTPS`
4. Add **Alternate Domain Names (CNAMEs)**:
   - `example.com`
   - `www.example.com` (optional)
5. Attach the **SSL Certificate** from ACM
6. Set **Default Root Object** to `index.html`
7. Click **Create Distribution**
8. Wait for deployment (~15 minutes)

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
   - Set it to redirect to `https://example.com`
   - Add a CloudFront distribution for it
   - Point `www.example.com` A record to this distribution

---

## ✅ Step 5: Test Everything

- Visit `https://example.com`
- Ensure your content loads securely
- Check SSL certificate validity
- Confirm you're served via CloudFront

---

## 🔐 Best Practices

- Enable **Origin Access Control (OAC)** to block direct S3 access
- Use **CloudFront Logging** for traffic analysis
- Set **Cache-Control headers** for performance

---

## 📌 Optional Enhancements

- Use **Terraform** or **AWS CDK** for infrastructure-as-code setup
- Add **custom error pages**
- Enable **WAF (Web Application Firewall)** for protection

---
