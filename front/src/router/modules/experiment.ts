const experiment: AuthRoute.Route = {
  name: 'experiment',
  path: '/experiment',
  component: 'self',
  meta: { title: '模型实验', icon: 'mdi:menu', singleLayout: 'basic', order: 2 },
  children: [
    {
      name: 'experiment_pages',
      path: '/experiment/pages',
      component: 'multi',
      meta: { title: 'experiment_pages', icon: 'mdi:menu' },
      children: [
        {
          name: 'experiment_pages_edit-page',
          path: '/experiment/pages/edit-page',
          component: 'self',
          meta: { title: 'experiment_pages_edit-page', icon: 'mdi:menu' }
        },
        {
          name: 'experiment_pages_detail-pages',
          path: '/experiment/pages/detail-pages',
          component: 'self',
          meta: { title: 'experiment_pages_detail-pages', icon: 'mdi:menu' }
        }
      ]
    }
  ]
};

export default experiment;
