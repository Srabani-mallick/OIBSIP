from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
def temperature_converter(request):
    if request.method == 'POST':
        try:
            temperature = float(request.POST['temperature'])
            from_unit = request.POST['from_unit']
            to_unit = request.POST['to_unit']
            converted_temp = convert_temperature(temperature, from_unit, to_unit)
            result = {
                'success': True,
                'converted_temp': round(converted_temp, 2),
                'from_unit': from_unit,
                'to_unit': to_unit
            }
            return JsonResponse(result)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Please enter a valid number!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Conversion failed!'})
    
    return render(request, 'converter/convert.html')
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == 'F':
        celsius = (temp - 32) * 5 / 9
    elif from_unit == 'K':
        celsius = temp - 273.15
    else:  
        celsius = temp
    if to_unit == 'F':
        return celsius * 9 / 5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:   
        return celsius
