from selenium.webdriver.common.by import By

from nicegui import ui

from .screen import Screen


def test_change_chart_series(screen: Screen):
    chart = ui.chart({
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')

    def update():
        chart.options['series'][0]['data'][:] = [1, 1]
        chart.update()

    ui.button('Update', on_click=update)

    def get_series_0():
        return screen.selenium.find_elements(By.CSS_SELECTOR, '.highcharts-series-0 .highcharts-point')

    screen.open('/')
    screen.wait(0.5)
    before = [bar.size['width'] for bar in get_series_0()]
    screen.click('Update')
    screen.wait(0.5)
    after = [bar.size['width'] for bar in get_series_0()]
    assert before[0] < after[0]
    assert before[1] < after[1]


def test_adding_chart_series(screen: Screen):
    chart = ui.chart({
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [],
    }).classes('w-full h-64')

    def add():
        chart.options['series'].append({'name': 'X', 'data': [0.1, 0.2]})
        chart.update()
    ui.button('Add', on_click=add)

    screen.open('/')
    screen.click('Add')
    screen.wait(0.5)
    assert len(screen.selenium.find_elements(By.CSS_SELECTOR, '.highcharts-point')) == 3


def test_removing_chart_series(screen: Screen):
    chart = ui.chart({
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')

    def remove():
        chart.options['series'].pop(0)
        chart.update()
    ui.button('Remove', on_click=remove)

    screen.open('/')
    screen.click('Remove')
    screen.wait(0.5)
    assert len(screen.selenium.find_elements(By.CSS_SELECTOR, '.highcharts-point')) == 3
