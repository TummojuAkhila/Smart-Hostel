# Smart Hostel Stay - Pre-Deployment Checklist

## ✅ Code Preparation
- [x] Updated `settings.py` for production (DEBUG, ALLOWED_HOSTS, database)
- [x] Created `Procfile` with build and start commands
- [x] Created `render.yaml` for Render configuration
- [x] Updated `requirements.txt` with production dependencies
- [x] Created `.env.example` template
- [x] Set `runtime.txt` to Python 3.11

## 🔑 Generate Secret Key
Before deploying, generate a secure SECRET_KEY:

**On Windows (PowerShell):**
```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**On Linux/Mac:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copy the output and save it safely.

## 📋 Before Deploying to Render

1. **Push code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for production deployment to Render"
   git push origin main
   ```

2. **Have these values ready:**
   - Generated SECRET_KEY (from above)
   - Your domain name
   - Your GitHub repository URL

3. **Create Render Account:**
   - Go to https://render.com
   - Sign up or log in

## 🚀 Quick Deployment Steps

1. In Render, create new Web Service from your GitHub repo
2. Set these environment variables:
   - `SECRET_KEY` = Your generated key
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `yourdomain.com,www.yourdomain.com,yourdomain.onrender.com`
3. Add PostgreSQL database
4. Deploy!
5. Connect your domain
6. View site at your domain URL

## 📚 Full Details
See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete step-by-step instructions.

## ⚠️ Important Notes
- Render auto-runs migrations from Procfile (release phase)
- Static files are collected during build
- First deploy may take 3-5 minutes
- Free tier includes one web service + one database
- Upgrade if you need better performance/uptime

---
Ready to deploy? Follow the steps in DEPLOYMENT_GUIDE.md!
