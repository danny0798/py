@echo off 
::�뽫��ͬ���ļ���������������ͬһ��Ŀ¼��
set /p var=������Ҫ���Ƶ��ļ�����(�����ʽ��*.txt;*.pdf):  
set /p path=������Ҫ���Ƶ���Ŀ���ļ���·��:
::ʹ��forѭ����ѯ��ǰ�������ļ��е�%var%�����ļ��������Ƶ�ָ��·���¡� 
 for /f "delims=" %%a in ('dir /a-d /b /s %var%') do ( 
    if not defined %%~nxa (  
      copy "%%a" "%path%"&set "%%~nxa=a" 
    ) else ( 
      set /a n+=1 
      ren "%path%\%%~nxa" "%%~na!n!%%~xa"&copy "%%a" "%path%" 
    ) 
) 
pause