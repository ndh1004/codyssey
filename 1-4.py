def sphere_area(diameter, material='유리', thickness=1):
    
    density = {'유리': 2.4, '알루미늄': 2.7, '탄소강': 7.85}    #재질의 무게
    MARS_GRAVITY_RATIO = 0.376  # 화성의 중력
    
    try:
        diameter = float(diameter)
        thickness = float(thickness)
        if diameter <= 0 or thickness <= 0:
            raise ValueError
    except ValueError:
        print('지름과 두께는 0보다 커야 하며, 숫자로 입력해야 합니다.')
        return 0, 0
    
    if material not in density:
        print('올바른 재질을 입력하세요: 유리, 알루미늄, 탄소강')
        return 0, 0
    
    radius = diameter / 2  # 반지름
    area = 2 * 3.14159265359 * (radius ** 2)  # 반구 면적
    volume = area * (thickness / 100)  # cm를 m로 변환
    weight = volume * density[material] / 1000  # g을 kg로 변환
    weight *= MARS_GRAVITY_RATIO  # 화성 중력 적용
    
    return round(area, 3), round(weight, 3)

while True:
    
    diameter = input('돔의 지름(m)을 입력하세요 (종료: exit): ')
    if diameter.lower() == 'exit':
        break
    material = input('재질을 입력하세요 (유리, 알루미늄, 탄소강) (종료: exit): ')
    if material.lower() == 'exit':
        break
    thickness = input('두께(cm)를 입력하세요 (종료: exit): ')
    if thickness.lower() == 'exit':
        break
    area, weight = sphere_area(diameter, material, thickness)
    if area > 0:
        print(f'\n재질 ==> {material}, 지름 ==> {diameter}, 두께 ==> {thickness}, 면적 ==> {area}, 무게 ==> {weight} kg\n')
