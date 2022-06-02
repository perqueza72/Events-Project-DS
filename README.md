# Install virtual env
virtualenv venv

python3 -m pip install --user virtualenv

source venv/bin/activate



# Para activar las variables de estado. 
source secret.env 



# Install requirenments
pip install -r requirements.txt 


# Errores en la instalación
Si instalar psycopg2 da error, solucionar usando el siguiente comando:

sudo apt install libpq-dev