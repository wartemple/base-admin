import { request } from '../request';

/**
 * 创建实验配置模板
 * @param name - 配置模板名称
 */
export function createExperimentConfigTemplateApi(name: string) {
  return request.post<ApiAuth.Token>('/api/experiment/config_templates/', { name });
}
