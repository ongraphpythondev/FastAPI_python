import pytest
import requests
import json

# Make sure Server is working when test/using this test_api.py file.


data1 = {
        "name" : "Jake",
        "age" : 15,
        "year" : "year 6"
    }
data2 = {
        "name" : "Tim",
        "age" : 22,
        "year" : "year 12"
}


@pytest.mark.parametrize("id,data",[(1,data1),(5,data2)])
def test_createstudentapi(id , data):
    url = "http://localhost:8000/create-student/"+str(id)+"/"
    response = requests.post(url,json=data)
    print(response.text)
    assert response.status_code == 200


@pytest.mark.parametrize("id" , [(1),(2),(3)])
def test_getstudentapi(id):
    url = "http://localhost:8000/get-student/"+str(id)+"/"
    response = requests.get(url)
    assert response.status_code ==200
    
