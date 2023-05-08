import os, shutil, time

def update_frontend(repository, project):
    ADMIN = 'juancamr'
    
    start = time.time()
    os.system('sudo su')
    exists = os.path.exists(f'./{repository}')

    if (not exists):
        os.system(f'git clone https://github.com/{ADMIN}/{repository}')
        install_modules(repository, project)
    else:
        os.chdir(f'./{repository}')
        os.system('git pull')
        os.system('npm install')
        os.system('ng build')
        os.system(f'cp -r ./dist /var/www/html/Grupo/{project}/dist')

        end = time.time()
        print(f'Pagina actualizada en {round(end - start)} segundos.')

def install_modules(repository, project):
    os.chdir(f'./{repository}')
    os.system('npm install')
    os.chdir('../')
    update_frontend(repository, project)