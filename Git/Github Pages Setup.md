# Setting Up GitHub Pages for a Repository

Follow these steps to set up **GitHub Pages** for a repository hosted on GitHub.

---

## **Step 1: Push Your Code to GitHub**

Ensure that your project is in a GitHub repository. If it isn't already, initialize a Git repository and push it:

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main  # Ensure you're on the main branch
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## **Step 2: Enable GitHub Pages**

1. **Go to Your Repository** on GitHub.
2. **Click on "Settings"** (top-right).
3. In the left sidebar, click **"Pages"**.
4. Under "Branch," select:
   - **Branch:** `main` (or the branch you want to use)
   - **Folder:** Choose `/ (root)` or `/docs` (if your site is inside a `docs` folder).
5. Click **"Save"**.

---

## **Step 3: Wait for Deployment**

- GitHub will automatically deploy your site.
- After a few minutes, your site will be live at:

  ```
  https://YOUR_USERNAME.github.io/YOUR_REPO/
  ```

---

## **Step 4: (Optional) Use a Custom Domain**

1. Go to **Settings → Pages**.
2. Under "Custom domain," enter your domain (e.g., `yourdomain.com`).
3. Configure your **DNS settings**:
   - Add a **CNAME record** pointing to `YOUR_USERNAME.github.io`.
   - (For apex domains) Add **A records** pointing to GitHub’s IP addresses:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```

---

## **Step 5: (Optional) Use a Static Site Generator**

If you're using a static site generator (like React, Vue, Next.js, or Jekyll), you'll need to build the site and deploy the `dist` or `build` directory.

For example, in React:

```sh
npm run build
git add -A
git commit -m "Deploy React app"
git push origin main
```

Then, set **GitHub Pages** to serve from the `gh-pages` branch or the `build` folder.

---
