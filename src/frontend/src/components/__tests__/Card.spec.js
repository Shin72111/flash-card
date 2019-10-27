import { shallowMount } from '@vue/test-utils'
import Card from '../Card.vue'

describe('Card.vue', () => {
  test('renders Front face and Back face texts by default', () => {
    const wrapper = shallowMount(Card)
    expect(wrapper.text()).toContain('Front face')
    expect(wrapper.text()).toContain('Back face')
  })

  test('renders front slot correctly', () => {
    const wrapper = shallowMount(Card, {
      slots: {
        front: '<p>This is the front card info</p>'
      }
    })
    expect(wrapper.find('div.front').find('p').text()).toContain(
      'This is the front card info'
    )
  })

  test('renders back slot correctly', () => {
    const wrapper = shallowMount(Card, {
      slots: {
        back: '<p>This is the back card info</p>'
      }
    })
    expect(wrapper.find('div.back').find('p').text()).toContain(
      'This is the back card info'
    )
  })
  
  test('flipped is fault by default', () => {
    const wrapper = shallowMount(Card)
    expect(wrapper.vm.flipped).toBe(false)
  })

  test('card-content does not have flipped class when initialized', () => {
    const wrapper = shallowMount(Card)
    const cardContent = wrapper.find('.card-content')
    expect(cardContent.classes()).not.toContain('flipped')
  })

  test('adds flipped class to card-content when card is clicked', () => {
    const wrapper = shallowMount(Card)
    const card = wrapper.find('.card')
    const cardContent = wrapper.find('.card-content')

    card.trigger('click')
    expect(cardContent.classes()).toContain('flipped')
  })

  test('remove flipped class to card-content when card is clicked twice',
      () => {
    const wrapper = shallowMount(Card)
    const card = wrapper.find('.card')
    const cardContent = wrapper.find('.card-content')

    card.trigger('click')
    card.trigger('click')
    expect(cardContent.classes()).not.toContain('flipped')
  })
})

