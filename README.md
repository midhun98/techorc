### Step 1: Clone the Repository
```
https://github.com/midhun98/techorc.git
```

### Step 2: Create the .env File in Project Root
```
SECRET_KEY=SECRET_KEY
DEBUG=True
DB_ENGINE=django.db.backends.postgresql
DB_NAME=techorc
DB_USER=postgres
DB_PASSWORD=root
DB_HOST=postgres
DB_PORT=5432
```

### Step 3. Building a Docker Image
```
docker build -t techorc-app-image .
```

### Step 4. Build and Run the Containers
```
docker-compose up -d
```

### Step 5. Apply the migrations..
```
docker-compose exec app python manage.py migrate
```
