# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

import json

from .models import MachineData, MachineRegistration, UserLogin, ComponentRegistration, Assignment
# Create your views here.


# This method will be called for url = 127.0.0.1:8000/home/app1
# class ComponentDashboard(APIView):

#     def get(self, request):
#         # all_data = machine_registration.objects.all()
#         # print all_data
#         # for field in all_data:
#         #     print field.id, field.machine_number, field.machine_description

#         required_data = machine_registration.objects.get(machine_number=2)
#         print required_data.user_info.last_name
#         # print required_data.machine_description, required_data.machine_number
#         # print request.data

#         return Response("Done")


# API for URL: http://127.0.0.1:8000/componentdashboard/
class ComponentDashboard(APIView):

    def get(self, request):

        print 'In GET Method************************'
        component_number = request.GET.get('cno')
        print component_number
        comp = ComponentRegistration.objects.get(
            component_number=component_number)
        print component_number
        c = comp.id
        print c, "***************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        all_data = MachineData.objects.filter(
            component_number_id=c)
        print"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        data_list = []
        print all_data

        try:
            for field in all_data:
                print "fffffffffffffffffffffffffffffff", field.id, field.machine_number, field.component_number, field.pieces, field.cycle_time, field.created_at
                md = MachineRegistration.objects.get(
                    machine_number=field.machine_number).machine_description
                print md
                cd = ComponentRegistration.objects.filter(
                    component_number=field.component_number).latest("id").component_description
                print cd
                # cn = ComponentRegistration.objects.get(
                #     id=component_number).component_number
                # print cn
                # Use component_number(FK) from table machine_data,
                # cn = ComponentRegistration.objects.get(
                #     id=component_number).component_number
                # then go to table component_registration and get component
                # number

                data_list.append({
                    'machine_number': field.machine_number,
                    'machine_description': md,
                    'component_number': component_number,
                    'component_description': cd,
                    'time_date': field.created_at.ctime(),
                    'total_pieces': field.pieces,
                    'cycle_time': field.cycle_time
                })
                print data_list
        except Exception as e:

            print e
            print "ERROR"

        context = {'component_data': json.dumps(data_list)}
        print context
        return render(request, 'app_industry/component_dashboard.html',
                      context)

    def post(self, request):  # using post method
        component_number = request.data  # requesting component_number from the user
        print component_number
        all_data = MachineData.objects.filter(
            component_number=component_number)  # In database open machine_data and filter for component_number = C3
        data_list = []  # Create a datalist
        print all_data
        cn = ComponentRegistration.objects.get(
            id=component_number).component_number  # Use component_number(FK) from table machine_data,
        # then go to table component_registration and get component number
        print cn
        for field in all_data:  # For loop to get data of the component_number field from machine_data table
            print field.machine_number, field.pieces, field.cycle_time, field.created_at
            md = MachineRegistration.objects.get(
                machine_number=field.machine_number).machine_description  # Use machine_number(FK) from table machine_data,
            # then go to table machine_registration and get machine description
            print md
            # Append the requested component_number data is the data_list
            data_list.append({
                'machine_number': field.machine_number,
                'machine_description': md,
                'component_number': cn,
                'time_date': field.created_at.ctime(),
                'total_pieces': field.pieces,
                'cycle_time': field.cycle_time
            })

        return Response(data_list)  # Return/display the data_list


# API for URL: http://127.0.0.1:8000/machinedashboard/
class MachineDashboard(APIView):

    def get(self, request):

        print 'In GET Method************************'
        machine_number = request.GET.get('mno')
        print machine_number

        all_data = MachineData.objects.filter(machine_number=machine_number)
        data_list = []
        print all_data
        try:
            for field in all_data:
                print field.id, field.machine_number, field.running_time, field.downtime, field.component_number, field.pieces, field.stops, field.cycle_time
                md = MachineRegistration.objects.get(
                    machine_number=field.machine_number).machine_description
                print md
                cd = ComponentRegistration.objects.filter(
                    component_number=field.component_number).latest("id").component_description
                print cd

                data_list.append({
                    'machine_number': field.machine_number,
                    'machine_description': md,
                    'component_number': field.component_number.component_number,
                    'component_description': cd,
                    'time_date': field.created_at.ctime(),
                    'status': field.status,
                    'total_pieces': field.pieces,
                    'cycle_time': field.cycle_time,
                    'stops': field.stops,
                    'running_time': field.running_time,
                    'downtime': field.downtime
                })
                print data_list
        except Exception as e:

            print e
            print "ERROR"

        context = {'machine_data': json.dumps(data_list)}
        print context
        return render(request, 'app_industry/chart.html', context)

        # print 'In GET Method************************'
        # machine_number = request.GET.get('mno')
        # print machine_number
        # return render(request, 'app_industry/machine_table.html')

    def post(self, request):
        print 'requ=====================', request.data
        machine_number = request.data['machine_number']
        print machine_number
        all_data = MachineData.objects.filter(machine_number=machine_number)
        data_list = []
        print all_data
        try:
            for field in all_data:
                print field.id, field.machine_number, field.running_time, field.downtime, field.component_number, field.pieces, field.stops, field.cycle_time
                md = MachineRegistration.objects.get(
                    machine_number=field.machine_number).machine_description
                print md
                cd = ComponentRegistration.objects.filter(
                    component_number=field.component_number).latest("id").component_description
                print cd

                data_list.append(json.dumps({
                    'machine_number': machine_number,
                    'machine_description': md,
                    'component_number': field.component_number.component_number,
                    'component_description': cd,
                    'time_date': field.created_at.ctime(),
                    'total_pieces': field.pieces,
                    'cycle_time': field.cycle_time,
                    'running_time': field.running_time,
                    'downtime': field.downtime,
                    'stops': field.stops
                }))
                print data_list
        except:
            print "ERROR"

        return Response(data_list)


class Dashboard(APIView):  # API for URL: http://127.0.0.1:8000/dashboard/

    def get(self, request):
        all_data = MachineData.objects.all()
        data_list = []
        print all_data
        try:
            for field in all_data:
                print field.id, field.machine_number, field.running_time, field.downtime, field.component_number, field.pieces, field.stops, field.cycle_time
                md = MachineRegistration.objects.get(
                    machine_number=field.machine_number).machine_description
                print md
                cd = ComponentRegistration.objects.filter(
                    component_number=field.component_number).latest("id").component_description
                print cd

                data_list.append({
                    'machine_number': field.machine_number,
                    'machine_description': md,
                    'component_number': field.component_number.component_number,
                    'component_description': cd,
                    'time_date': field.created_at.ctime(),
                    'status': field.status,
                    'total_pieces': field.pieces,
                    'cycle_time': field.cycle_time,
                    'stops': field.stops
                })
                print data_list
        except Exception as e:

            print e
            print "ERROR"

        # return Response(data_list)
        context = {'machine_data': json.dumps(data_list)}
        print context
        return render(request, 'app_industry/home.html', context)


# # API for URL: http://127.0.0.1:8000/componentassignment/
# class ComponentAssign(APIView):

#     def post(self, request):
#         try:

#             comp_assign = ComponentAssign(
#                 component_number_id=request.data['c'],
#                 machine_number_id=request.data['m'])
#             print '///////////////////////////////////////////////', comp_assign
#             comp_assign.save()
#             response = "sucess"
#             print '////////////////////////////////////', comp_assign

#         except Exception as e:

#             print e
#             print "ERROR"
#             response = "fail"

#         return Response(response)


class List(APIView):  # API for URL: http://127.0.0.1:8000/list/

    def get(self, request):
        all_data = ComponentAssign.objects.all()
        data_list = []
        print all_data
        try:
            for field in all_data:
                print field.machine_number, field.component_number

                data_list.append({
                    'time_date': field.updated_at.ctime(),
                    'machine_number': field.machine_number.machine_number,
                    'machine_description': field.machine_number.machine_description,
                    'component_number': field.component_number.component_number,
                    'component_description': field.component_number.component_description,
                })
                print data_list
        except:
            print "ERROR"

        return Response(data_list)


class AssignmentDashboard(APIView):

    def get(self, request):
        a = MachineRegistration.objects.all()
        b = ComponentRegistration.objects.all()
        data_list1 = []
        data_list2 = []
        print'+++++++++++++++++++++++++++++++++++++++++++++++++++', a

        for field in a:
            print "+++++++++++++++++++++++++++++++", field.machine_number, field.machine_description

            data_list1.append({

                'machine_number': field.machine_number,
                'machine_description': field.machine_description,

            })

        for field in b:
            print "+++++++++++++++++++++++++++++++", field.component_number, field.component_description

            data_list2.append({

                'component_number': field.component_number,
                'component_description': field.component_description,

            })

        # return Response(data_list)
        context = {'assign_machine_data': json.dumps(
            data_list1), 'assign_component_data': json.dumps(data_list2)}
        print context
        return render(request, 'app_industry/card.html', context)

    def post(self, request):
        try:

            all_data = Assignment(component_number_id=request.data[
                                  'c'], machine_number_id=request.data['m'])
            all_data.save()
            response = "Sucess"
        except Exception as e:
            print e
            print "ERROR"
            response = "Fail"

        return Response(response)


class AddComponent(APIView):  # API for URL: http://127.0.0.1:8000/addcomponent/

    def post(self, request):

        try:

            add_comp = ComponentRegistration(
                component_number=request.data['component_number'],
                component_description=request.data['component_description'])
            add_comp.save()
            response = "sucess"

        except:
            print "ERROR"
            response = "fail"

        return Response(response)


class UserLogin(APIView):  # API for URL: http://127.0.0.1:8000/userlogin/

    def post(self, request):
        username = request.data["u"]
        password = request.data["p"]
        print username, password
        all_data = UserLogin.objects.all()
        print all_data
        for field in all_data:
            print field.username, field.password

            if (username == field.username) and (password == field.password):
                response = "Success"
                break
            else:
                response = "Fail"

        return Response(response)


class SensorData(APIView):  # API for URL: http://127.0.0.1:8000/sensordata/

    def post(self, request):
        machine_number = request.data["machine_number"]
        pieces = request.data["pieces"]
        status = request.data["status"]
        cycle_time = request.data["cycle_time"]
        stops = request.data["stops"]
        running_time = request.data["running_time"]
        downtime = request.data["downtime"]

        machine = MachineRegistration.objects.get(
            machine_number=machine_number)
        print machine
        mach = machine.id
        print "machien status", mach
        component = ComponentAssignment.objects.filter(
            machine_number_id=mach).latest("id")
        component_ids = component.component_number_id
        print "component status", component_ids

        machine_record = MachineData(machine_number=machine_number, component_number_id=component_ids,
                                     pieces=pieces, status=status, cycle_time=cycle_time,
                                     stops=stops, running_time=running_time, downtime=downtime)

        machine_record.save()

        return Response('machine_record')
