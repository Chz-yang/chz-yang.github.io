python tools/process_img_url_before_publish.py

git add .
git commit -m "update article"
git push

cd static/images
git add .
git commit -m "update images"
git push
