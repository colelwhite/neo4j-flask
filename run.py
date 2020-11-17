from plant_app import plant_app
import os

if __name__ == '__main__':

    # Execute the web app
    # Setting the secret key allows you to use sessions
    plant_app.secret_key = os.urandom(24)
    plant_app.run(host='0.0.0.0', port=4545, debug=True)
