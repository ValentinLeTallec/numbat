<!-- This file is autogenerated! Do not modify it -->

# Body mass index
<a href="https://numbat.dev/?q=%23+This+script+calculates+the+Body+Mass+Index+%28BMI%29+based+on%0A%23+the+provided+mass+and+height+values.%0A%0Aunit+BMI%3A+Mass+%2F+Length%5E2+%3D+kg+%2F+m%5E2%0A%0Afn+body_mass_index%28mass%3A+Mass%2C+height%3A+Length%29+%3D%0A++++mass+%2F+height%C2%B2+-%3E+BMI%0A%0Aprint%28body_mass_index%2870+kg%2C+1.75+m%29%29%0A"><i class="fa fa-play"></i> Run this example</a>

``` numbat
# This script calculates the Body Mass Index (BMI) based on
# the provided mass and height values.

unit BMI: Mass / Length^2 = kg / m^2

fn body_mass_index(mass: Mass, height: Length) =
    mass / height² -> BMI

print(body_mass_index(70 kg, 1.75 m))
```
