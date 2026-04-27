# Deployment Guide — SME Risk Register

This guide walks you through deploying your Risk Register tool. Total time: **~15 minutes**.

You will end up with:
- A public website at `https://YOUR-NAME.github.io/sme-risk-register` (free)
- An API backend at `https://YOUR-APP.up.railway.app` ($5/month after free trial)
- A working tool people can use to download tailored Excel risk registers

---

## Before you start

You'll need:
- An email address
- A web browser
- A bank card (Railway requires this even for the free tier — they don't charge unless you exceed the free hours)

You do NOT need any technical knowledge.

---

## Step 1 — Create a GitHub account (2 minutes)

GitHub stores your code and serves the frontend website for free.

1. Go to **[github.com/signup](https://github.com/signup)**
2. Enter your email, choose a password, pick a username (e.g. `acme-pty-ltd`)
3. Verify your email when prompted

✅ Done.

---

## Step 2 — Create a new repository (2 minutes)

1. Once logged in, click the **+** icon in the top right → **"New repository"**
2. Name it: `sme-risk-register`
3. Set it to **Public**
4. Tick the box **"Add a README file"**
5. Click **"Create repository"**

✅ You now have a place to store your code.

---

## Step 3 — Upload the project files (3 minutes)

1. On your new repository's page, click **"Add file"** → **"Upload files"**
2. Drag the entire `sme-risk-register` folder contents into the upload area
   - You should see: `frontend/`, `backend/`, `README.md`, `DEPLOY.md`, `.gitignore`
3. Scroll down and click **"Commit changes"**

✅ Your code is now on GitHub.

---

## Step 4 — Deploy the backend on Railway (5 minutes)

Railway runs your Python API.

1. Go to **[railway.app](https://railway.app)**
2. Click **"Login"** → **"Login with GitHub"** → authorise Railway to access your GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Find and select **`sme-risk-register`** from the list
5. Railway will detect the Python project and start building

   ⚠️ **Important**: Railway needs to know to use the `backend/` folder, not the root.
   - Click your project → **"Settings"** → **"Source"**
   - Set **Root Directory** to: `backend`
   - Click **"Save"**
   - Click **"Deploy"** (or wait for it to redeploy automatically)

6. Once you see a green "Deployed" status, click **"Settings"** → **"Networking"** → **"Generate Domain"**
7. Copy the URL Railway gives you (it'll look like `sme-risk-register-production.up.railway.app`)

✅ Your backend is live.

---

## Step 5 — Connect the frontend to the backend (2 minutes)

Now we tell the website where the API lives.

1. Back on GitHub, navigate to `frontend/index.html` in your repository
2. Click the pencil icon (✏️) to edit the file
3. Find this line near the top of the `<script>` section:
   ```js
   : 'https://YOUR-RAILWAY-URL.up.railway.app';
   ```
4. Replace `YOUR-RAILWAY-URL.up.railway.app` with the URL you copied from Railway in Step 4
   - For example: `'https://sme-risk-register-production.up.railway.app'`
5. Scroll down and click **"Commit changes"**

✅ Frontend and backend are connected.

---

## Step 6 — Enable GitHub Pages (1 minute)

This publishes your website.

1. On your repository page, click **"Settings"** (top right)
2. In the left sidebar, click **"Pages"**
3. Under **"Source"**, select **"Deploy from a branch"**
4. Under **"Branch"**, select `main` and `/frontend` folder (or `/(root)` if `/frontend` isn't available — see note below)
5. Click **"Save"**
6. Wait 1-2 minutes for deployment, then refresh — you'll see a green box with your URL: `https://YOUR-USERNAME.github.io/sme-risk-register`

📝 **If `/frontend` isn't an option**: GitHub Pages can only serve from `/` or `/docs`. Move the contents of `frontend/` into `/docs/` instead, then choose `/docs`. Or use Netlify (simpler but separate signup).

✅ **Your tool is live!** Test it by visiting your GitHub Pages URL and clicking through the configurator.

---

## Optional: Custom domain (10 minutes)

Make it look properly professional with `riskregister.yourfirm.com`.

1. Buy a domain from any registrar (Namecheap, GoDaddy, Hover — about $15/year)
2. **For GitHub Pages**: In your repo Settings → Pages → Custom domain, enter your domain. Then add a CNAME record in your domain registrar pointing to `YOUR-USERNAME.github.io`
3. **For Railway**: Settings → Domains → Add Custom Domain, follow Railway's CNAME instructions

---

## Maintenance

- **To update the tool**: Edit any file on GitHub directly, click commit. Both the website and API auto-redeploy.
- **To check the API is healthy**: Visit `https://YOUR-RAILWAY-URL.up.railway.app/health`
- **Free tier limits**: GitHub Pages is unlimited for public repos. Railway gives ~$5 of free credit/month, which is enough for thousands of register downloads.

---

## Troubleshooting

**The website loads but the download button shows an error**
→ The backend URL in `frontend/index.html` is wrong. Re-do Step 5 with the exact URL from Railway.

**Railway build fails**
→ Make sure Root Directory is set to `backend` (not blank or `/`). Re-check Step 4.

**GitHub Pages shows a 404**
→ Check Settings → Pages — branch must be `main`, folder must contain your `index.html`. Wait 2-3 minutes after enabling.

**Excel file downloads but won't open**
→ Open Railway logs (Project → Deployments → View Logs) to see the Python error. Most likely a missing dependency — verify `backend/requirements.txt` is present.

---

Need help? Open an issue on the GitHub repository or contact the original developer.
