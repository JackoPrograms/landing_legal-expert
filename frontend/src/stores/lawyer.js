import { defineStore } from 'pinia'
import api from '../services/api'

export const useLawyerStore = defineStore('lawyer', {
  state: () => ({
    services: [],
    lawyers: [],
    reviews: [],
    articles: [],
    heroSlides: [],
    companyInfo: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchServices() {
      try {
        this.loading = true
        const response = await api.getServices()
        this.services = response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки услуг'
        console.error('Error fetching services:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchLawyers() {
      try {
        this.loading = true
        const response = await api.getLawyers()
        this.lawyers = response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки юристов'
        console.error('Error fetching lawyers:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchReviews() {
      try {
        this.loading = true
        const response = await api.getReviews()
        this.reviews = response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки отзывов'
        console.error('Error fetching reviews:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchArticles(page = 1) {
      try {
        this.loading = true
        const response = await api.getArticles(page)
        this.articles = response.data.results || response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки статей'
        console.error('Error fetching articles:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchHeroSlides() {
      try {
        this.loading = true
        const response = await api.getHeroSlides()
        this.heroSlides = response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки слайдов'
        console.error('Error fetching hero slides:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchCompanyInfo() {
      try {
        this.loading = true
        const response = await api.getCompanyInfo()
        this.companyInfo = response.data
        this.error = null
      } catch (error) {
        this.error = 'Ошибка загрузки информации о компании'
        console.error('Error fetching company info:', error)
      } finally {
        this.loading = false
      }
    },

    async sendContactRequest(data) {
      try {
        this.loading = true
        const response = await api.sendContactRequest(data)
        this.error = null
        return response.data
      } catch (error) {
        this.error = 'Ошибка отправки заявки'
        console.error('Error sending contact request:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async loadAllData() {
      await Promise.all([
        this.fetchServices(),
        this.fetchLawyers(),
        this.fetchReviews(),
        this.fetchArticles(),
        this.fetchHeroSlides(),
        this.fetchCompanyInfo(),
      ])
    },
  },
})


