import { isDevelopment } from '@utils/isDev'
import { CliConfigurator, registerCommand } from '@/cli'
import { version, name } from '../../package.json'

export function getConfigurator(dev?: boolean): CliConfigurator {
  const IS_DEV = dev || isDevelopment()
  if (!IS_DEV) return registerCommand(version, name)
  return {
    global: {
      logLevel: 'info',
    },
    wx: {
      // appid: '',
      format: true,
      clearDecompile: true,
      clearSave: true,
      parse: true,
      depth: 1,
      // output: '',
      packages: ['files'],
    },
  }
}
