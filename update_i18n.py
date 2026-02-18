import os

file_path = 'index.html'
if not os.path.exists(file_path):
    print('Error: index.html 파일을 찾을 수 없습니다.')
else:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        '시네젠 듀얼': '<span data-i18n="header_title">CINE-GEN DUAL</span>',
        '소스 분석기': '<span data-i18n="section_analyzer">SOURCE ANALYZER</span>',
        '시나리오 지시문': '<span data-i18n="label_scenario">Scenario Directive</span>',
        '타겟 시네마틱 스타일': '<span data-i18n="label_style">Target Cinematic Style</span>',
        '듀얼 엔진 초기화': '<span data-i18n="btn_generate">INITIALIZE DUAL ENGINE</span>',
        '기술 감독의 노트': '<span data-i18n="td_note_title">Technical Director\'s Note</span>'
    }

    for ko, en_html in replacements.items():
        content = content.replace(ko, en_html)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('index.html 업데이트 완료! ✅')
