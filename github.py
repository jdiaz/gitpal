"""Provides functionalities for interacting with the Github API"""

import http.client
import configparser

#TODO: implement this module
class Github(object):


    def __init__(self):
        config = configparser.ConfigParser()
        config.read('gitpal.ini')
        props = config['API']
        self.AUTH_TOKEN = props['AUTH_TOKEN']
        self.GITHUB_API = props['GITHUB_API']


    def put_file_in_repo(self, file):
        # TODO: implement
        return None


    def create_repo(self, name, description):
        """Creates a new github repository with the given specifications

        Args:
            name: Repository name
            description: NOTES contents
        """
        # TODO: Implement
        headers = {
            'Content-Type': 'application/text',
            'Accept': 'text/plain',
            'Authorization': 'token {}'.format(self.AUTH_TOKEN),
        }
        params = {

        }
        conn = http.client.HTTPConnection(self.GITHUB_API)
        conn.request('POST', '', params, headers)
        response = conn.getresponse()
        if response.status == 200:
            return True

        return False


    def fetch_license(license):
        return ''


    def make_project():
        return ''
