@echo off 
::请将不同的文件夹与此批处理放在同一个目录下
set /p var=请输入要复制的文件类型(输入格式：*.txt;*.pdf):  
set /p path=请输入要复制到的目标文件夹路径:
::使用for循环查询当前所有子文件中的%var%类型文件，并复制到指定路径下。 
 for /f "delims=" %%a in ('dir /a-d /b /s %var%') do ( 
    if not defined %%~nxa (  
      copy "%%a" "%path%"&set "%%~nxa=a" 
    ) else ( 
      set /a n+=1 
      ren "%path%\%%~nxa" "%%~na!n!%%~xa"&copy "%%a" "%path%" 
    ) 
) 
pause