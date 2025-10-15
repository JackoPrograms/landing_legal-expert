import axios from 'axios'

// Создаем экземпляр axios с базовыми настройками
const api = axios.create({
  baseURL: '/api/lawyer',
  headers: {
    'Content-Type': 'application/json',
  },
})

// API методы
export default {
  // Услуги
  getServices() {
    return api.get('/services/')
  },
  
  getService(slug) {
    return api.get(`/services/${slug}/`)
  },
  
  // Юристы
  getLawyers() {
    return api.get('/lawyers/')
  },
  
  // Отзывы
  getReviews() {
    return api.get('/reviews/')
  },
  
  // Статьи
  getArticles(page = 1) {
    return api.get('/articles/', { params: { page } })
  },
  
  getArticle(slug) {
    return api.get(`/articles/${slug}/`)
  },
  
  // Слайды баннера
  getHeroSlides() {
    return api.get('/hero-slides/')
  },
  
  // Информация о компании
  getCompanyInfo() {
    return api.get('/company-info/')
  },
  
  // Заявки на консультацию
  sendContactRequest(data) {
    return api.post('/contact-requests/', data)
  },
}


