# Deploy Frontend and Backend to Netlify + Railway

## Tasks
- [x] Deploy backend to Render using existing render.yaml
- [x] Create render.yaml for frontend static site deployment
- [x] Update frontend JavaScript files to use the deployed backend URL
- [x] Fix render.yaml configuration issues (region, publishDir, staticSiteGenerator, plan, rootDir, buildCommand)
- [x] Deploy frontend to Render (Blueprint created, publishDir added)
- [x] Switch to Netlify + Railway (easier deployment)
- [x] Create netlify.toml for frontend deployment
- [x] Create railway.json for backend deployment
- [x] Update API_BASE_URL to Railway backend URL
- [x] Update CORS settings for Netlify domains
- [x] Add ignore rule to prevent Netlify rebuilds on backend changes
- [x] Remove old Vercel and Render config files to avoid confusion
- [x] Deploy frontend to Netlify (connect to GitHub repo)
- [x] Update all HTML files with Railway backend URL
- [x] Fix settings.py indentation error
- [x] Create admin user
- [x] Migrate database
- [x] Collect static files
- [x] Commit changes to git
- [x] Push code to GitHub
- [x] Deploy backend to Railway (add DJANGO_SUPERUSER_PASSWORD env var)
- [x] Deploy frontend to Netlify
- [x] Test the full deployment
- [x] Access admin panel at: https://your-railway-url/admin/
- [x] Frontend available at: https://prairesafricatravel.netlify.app/

## Notes
- Switched from Render to Netlify + Railway for easier deployment
- Netlify handles static frontend with automatic deployments
- Railway provides simple Django deployment with database
- All configurations created and committed to GitHub
- Ready for deployment to both platforms
- Updated all HTML files (booking.html, booking-new.html, payment-status.html, upload-proof.html, test-api.html) with Railway backend URL
- Fixed Django settings.py indentation issue
- Created admin user for backend
- Database migrations applied
- Static files collected for production
