from flask import Flask

from modules.account.account import account_api

app = Flask(__name__)

# Configure Application
###############################################################################

app.config.from_object('config.dev.config-dev.Development')

# Register Routes
###############################################################################

app.register_blueprint(account_api)

@app.route("/")
def welcome():
    return "Welcome to the Python Server to use Temenos!"

# Main Entry Point
###############################################################################

if __name__ == "__main__":
    port = 8080
    
    print('Launching Server on port {}...'.format(port))
    
    print('\n*** CONFIG ***\n')
    print('Temenos Config:')
    print('  - HOST : {}'.format( app.config['TEMENOS_HOST'] ))
    print('  - USER : {}'.format( app.config['TEMENOS_USER'] ))
    print()
    
    app.run(port = port)