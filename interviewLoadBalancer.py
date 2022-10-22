import pytest
import random

class Not_Unique(Exception):
    pass

class Too_Many_Instances(Exception):
    pass

class Not_Valid_Instance(Exception):
    pass

class LoadBalancer():

    def __init__(self):
        self.listOfInstances = []

    def _check_if_instance_is_unique(self, new_instance):
        for instance in self.listOfInstances:
            if instance.ipAddress == new_instance.ipAddress:
                raise Not_Unique("The new instance is not unique")

    def _check_if_there_are_too_many_instances(self):
        if len(self.listOfInstances) >= 10:
            raise Too_Many_Instances("Too many instances")

    def _check_if_it_is_a_valid_instance(self, new_instance):
        if not new_instance:
            raise Not_Valid_Instance("Not a valid one")

    def addInstance(self, new_instance):
        self._check_if_it_is_a_valid_instance(new_instance)
        self._check_if_instance_is_unique(new_instance)
        self._check_if_there_are_too_many_instances()

        self.listOfInstances.append(new_instance)
        # add possibility to add a list of instances

    def get(self):
        return random.choice(self.listOfInstances)

    def __str__(self):
        return str([instance.ipAddress for instance in self.listOfInstances])

class Instance():
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
    def __str__(self):
        return self.ipAddress

def test_at_most_10_instances():

    listOfInstances = [Instance(f"{i}") for i in range(1,12)]

    loadBalancer = LoadBalancer()

    with pytest.raises(Too_Many_Instances):
        for instance in listOfInstances:
            loadBalancer.addInstance(instance)

def test_check_for_uniqueness():
    a = Instance("192.168.0.1")
    a_not_good = Instance("192.168.0.1")

    loadBalancer = LoadBalancer()
    loadBalancer.addInstance(a)

    with pytest.raises(Not_Unique):
        loadBalancer.addInstance(a_not_good)

def test_a_invalid_instance():
    loadBalancer = LoadBalancer()
    with pytest.raises(Not_Valid_Instance):
        loadBalancer.addInstance(None)


def test_a_valid_instance():
    a = Instance("192.168.9.1")

    loadBalancer = LoadBalancer()
    loadBalancer.addInstance(a)

    assert len(loadBalancer.listOfInstances) == 1
    assert loadBalancer.listOfInstances.pop() == a


# def test_invoking_load_balancer_empty_sequence():
#     loadBalancer = LoadBalancer()
#     loadBalancer.get()

def test_invoking_load_balancer():
    random.seed(1)
    loadBalancer = LoadBalancer()
    a = Instance("192.168.9.1")
    b = Instance("192.168.1.1")
    c = Instance("192.168.1.3")

    loadBalancer.addInstance(a)
    loadBalancer.addInstance(b)
    loadBalancer.addInstance(c)

    assert loadBalancer.get() == a