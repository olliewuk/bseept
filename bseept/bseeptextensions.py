#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Get the extensions installed
#
def getextensions(APIURL,APIKEY, doprint=True, output=False):
 
    query = '''
        query GetExtensions {
            extensions {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
                }
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Get the extension JAR file name
#
def updateextensionname(APIURL, APIKEY, id, name, doprint=True, output=False):
    query = '''

     mutation UpdateCustomExtensionName($id: ID!, $name: String!) {
        update_custom_extension_name (
            input: {
                id: $id
                name: $name
            }

        )

        {
            extension {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
                }
            }
        }
    }
    '''

    variables = {
        "id": id,
        "name": name
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update the extension description
#
def updateextensiondescription(APIURL, APIKEY, id, description, doprint=True, output=False):
    query = '''

     mutation UpdateCustomExtensionDescription($id: ID!, $desc: String!) {
        update_custom_extension_description (
            input: {
                id: $id
                description: $desc
            }

        )

        {
            extension {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
                }
            }
        }
    }
    '''

    variables = {
        "id": id,
        "desc": description
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result


#
# Upload a custom (none BApp) extension - assume b64jar contains the BASE64 encoded blob
#
def uploadcustomeextension(APIURL, APIKEY, filename, b64jar, name, description, doprint=True, output=False):
    query = '''

     mutation UploadCustomExtension($filename: String!, $b64jar: String!, $name: String!, $desc: String!) {
        upload_custom_extension (
            input: {
                extension_filename: $filename
                extension_jar_as_base_64: $b64jar
                name: $name
                description: $desc
            }

        )

        {
            extension {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
                }
            }
        }
    }
    '''

    variables = {
        "filename": filename,
        "b64jar": b64jar,
        "name": name,
        "desc": description
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result
