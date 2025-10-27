# Set up development server
Clone the repo
```
git clone https://github.com/toanhminh0412/mystore.git
cd mystore
```

From now on, `mystore` will be our root directory. Install python packages into a virtual environment:
```
pythom3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Create necessary environment variables. Create `mystore/.env`:
```
SECRET_KEY=supersecretkey       # Please change this to something secure. You can genereate one by running 'python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"'
DEBUG=true
ALLOWED_HOSTS=localhost,127.0.0.1
```

Perform a database migration:
```
python3 manage.py migrate
```

**(Optional)** Generate data for the app. If you want to use the Django's admin dashboard to manually create data, feel free to skip this step. Use the `populatedata` management command to generate test data (You can modify `data/products.json` to make changes to the data):
```
python3 manage.py populatedata
```

Run Django's development server on port 8000:
```
python3 manage.py runserver
```
or on other port (e.g. 4001):
```
python3 manage.py runserver 127.0.0.1:4001
```
Visit the app on `http://127.0.0.1:<port>`.
