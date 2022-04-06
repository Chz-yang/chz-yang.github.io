@REM 创建图片目录的软链
if not exist "static/images" (
    mklink /D .\static\images ..\images
)

.\hugo server --disableFastRender
