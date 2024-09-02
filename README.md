# python-todo-list
This is the basic python todo list in our python SDK demo. Feel free to play around with it yourself! It is super basic :)

Be sure to install the Fortress python SDK (https://github.com/fortress-build/sdk-python)


## Installation
```bash
pip install fortress-sdk-python
```

## Process to get started
```bash
git clone https://github.com/fortress-build/python-todo-list.git
```

## Add your organizationID, API key, and tenant_ID
```python
#[TODO]Fill in the org_id and api_key
client = Fortress(
    org_id='your-org-id', 
    api_key='your-api-key')


#[TODO]Insert a tenantID here
conn = client.connect_tenant(tenant_id='your-tenant-id')

```

## Run the program
```bash
python app.py
```