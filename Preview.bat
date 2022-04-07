@REM clone并更新图片目录
if not exist "static/images" (
    git clone git@github.com:Chz-yang/GitHubPageImages.git static/images
)
cd static/images
git pull .
cd ../../

@REM 创建图片目录的软链
if not exist "images" (
    mklink /D .\images .\static\images
)

@REM 更新所有GitHub子模块
git submodule update --init --recursive

.\hugo server --disableFastRender
