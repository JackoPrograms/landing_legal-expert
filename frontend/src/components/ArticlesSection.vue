<template>
  <section id="articles" class="section articles-section">
    <div class="container">
      <h2 class="section-title">Полезные материалы</h2>
      
      <div v-if="loading" class="loading">Загрузка статей...</div>
      
      <div v-else class="articles-grid">
        <div v-for="article in articles.slice(0, 3)" :key="article.id" class="article-card">
          <div class="article-image-wrapper">
            <img v-if="article.image" :src="article.image" :alt="article.title" class="article-image" />
            <div class="article-overlay">
              <span class="view-icon">👁</span>
            </div>
          </div>
          <div class="article-content">
            <div class="article-meta">
              <span class="article-date">{{ formatDate(article.published_date) }}</span>
              <span class="article-views">👁 {{ article.views }}</span>
            </div>
            <h3 class="article-title">{{ article.title }}</h3>
            <p class="article-excerpt">{{ article.excerpt }}</p>
            <a :href="`#article-${article.slug}`" class="article-link">Читать далее →</a>
          </div>
        </div>
      </div>
      
      <div v-if="articles.length > 3" class="articles-footer">
        <button class="btn btn-outline">Все материалы</button>
      </div>
    </div>
  </section>
</template>

<script>
import { onMounted } from 'vue'
import { useLawyerStore } from '../stores/lawyer'
import { storeToRefs } from 'pinia'

export default {
  name: 'ArticlesSection',
  setup() {
    const store = useLawyerStore()
    const { articles, loading } = storeToRefs(store)

    onMounted(() => {
      if (articles.value.length === 0) {
        store.fetchArticles()
      }
    })

    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      })
    }

    return {
      articles,
      loading,
      formatDate,
    }
  },
}
</script>

<style scoped>
.articles-section {
  background: var(--bg-light);
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  margin-bottom: 40px;
}

.article-card {
  background: var(--white);
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition-normal);
  display: flex;
  flex-direction: column;
}

.article-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-4px);
}

.article-image-wrapper {
  position: relative;
  width: 100%;
  height: 220px;
  overflow: hidden;
}

.article-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: var(--transition-normal);
}

.article-card:hover .article-image {
  transform: scale(1.1);
}

.article-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(74, 144, 226, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: var(--transition-normal);
}

.article-card:hover .article-overlay {
  opacity: 1;
}

.view-icon {
  font-size: 48px;
  color: var(--white);
}

.article-content {
  padding: 25px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  font-size: 14px;
  color: var(--text-light);
}

.article-date {
  color: var(--primary-color);
}

.article-views {
  display: flex;
  align-items: center;
  gap: 5px;
}

.article-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 15px;
  color: var(--dark-color);
  line-height: 1.3;
}

.article-excerpt {
  color: var(--text-light);
  line-height: 1.6;
  margin-bottom: 20px;
  flex: 1;
}

.article-link {
  color: var(--primary-color);
  font-weight: 600;
  transition: var(--transition-fast);
}

.article-link:hover {
  color: var(--primary-hover);
}

.articles-footer {
  text-align: center;
}

/* Responsive */
@media (max-width: 992px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .articles-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .article-content {
    padding: 20px;
  }
}
</style>


