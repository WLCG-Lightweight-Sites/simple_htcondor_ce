import argparse
import yaml
from files.site_security_59 import SiteSecurity59


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site_config', help="Compiled Site Level Configuration YAML file")
    parser.add_argument('--execution_id', help="Execution ID of lightweight component")
    parser.add_argument('--output_dir', help="Output directory")
    args = parser.parse_args()
    return {
        'augmented_site_level_config_file': args.site_config,
        'execution_id': args.execution_id,
        'output_dir': args.output_dir
    }


if __name__ == "__main__":
    args = parse_args()
    execution_id = args['execution_id']
    augmented_site_level_config_file = args['augmented_site_level_config_file']
    output_dir = args['output_dir']

    augmented_site_level_config = yaml.safe_load(open(augmented_site_level_config_file, 'r'))

    # Files present in container by default at /etc/condor-ce/config.d/: 01-ce-auth.conf  01-ce-router.conf
    # 01-common-auth.conf  02-ce-condor.conf  03-ce-shared-port.conf  03-managed-fork.conf

    # Custom config files
    site_security_59 = SiteSecurity59("{output_dir}/59_site_security.conf".format(output_dir=output_dir), augmented_site_level_config, execution_id)
    site_security_59.generate_output_file()

    configured_attributes_60 = ConfiguredAttributes60("{output_dir}/60_configured_attributes.conf".format(output_dir=output_dir), augmented_site_level_config, execution_id)

    
    # condor_mapfile = ConfigFile("{output_dir}/condor_mapfile".format(output_dir=output_dir), augmented_site_level_config)
    # condor_mapfile.add_categories(condor_mapfile_categories.get(augmented_site_level_config, execution_id))
    # condor_mapfile.generate_output_file()