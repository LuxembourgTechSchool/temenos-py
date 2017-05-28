from flask import current_app as app

import requests

class Temenos():
    
    def __init__(self):
        self.auth = ( app.config['TEMENOS_USER'], app.config['TEMENOS_PASSWORD'] )
        self.host = app.config['TEMENOS_HOST']
        
    def get_accounts(self):
        return self._do_get_request('verAccount_Tcibs()')
    
    def get_account(self, account_id):
        return self._do_get_request('enqTcibAcctDetailss({})'.format(account_id))
    
    def __prepare_session(self):
        s = requests.Session()
        s.auth = self.auth
        s.headers.update({'Accept': 'application/hal+json' , 'Content-Type': 'application/hal+json'})
        
        return s
    
    def _do_get_request(self, api):
        s = self.__prepare_session()
        
        r = s.get('{}/TCMBCommon-iris/TCMBCommon.svc/GB0010001/{}'.format( self.host, api ) )
        
        return r
