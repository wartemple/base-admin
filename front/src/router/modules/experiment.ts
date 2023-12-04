const experiment: AuthRoute.Route = {
  name: 'experiment',
  path: '/experiment',
  component: 'basic',
  meta: { title: 'experiment', icon: 'mdi:menu', order: 2 },
  children: [
    {
      name: 'experiment_list-page',
      path: '/experiment/list-page',
      component: 'self',
      meta: { title: '列表页', icon: 'mdi:menu' }
    },
    {
      name: 'experiment_form-page',
      path: '/experiment/form-page',
      component: 'self',
      meta: { title: '表单页', icon: 'mdi:menu' }
    },
    {
      name: 'experiment_detail-page',
      path: '/experiment/detail-page',
      component: 'self',
      meta: { title: '详情页', icon: 'mdi:menu' }
    }
  ]
};

export default experiment;
