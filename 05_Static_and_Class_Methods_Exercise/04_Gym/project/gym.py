from customer import Customer
from trainer import Trainer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__add_entity(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.add_subscription(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_entity_by_id(self.subscriptions, subscription_id)
        customer = self.__find_entity_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_entity_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_entity_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_entity_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + '\n' + \
            repr(customer) + '\n' + \
            repr(trainer) + '\n' + \
            repr(equipment) + '\n' + \
            repr(plan)

    def __add_entity(self, collection, entity):
        if entity in collection:
            return
        collection.append(entity)

    def __find_entity_by_id(self, collection, entity_id):
        for entity in collection:
            if entity.id == entity_id:
                return entity
