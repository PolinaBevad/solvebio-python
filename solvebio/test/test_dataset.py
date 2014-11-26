from solvebio.resource import Dataset

from .helper import SolveBioTestCase


class DatasetTests(SolveBioTestCase):
    """
    Test Dataset, DatasetField, and Facets
    """

    def test_dataset_retrieval(self):
        dataset = Dataset.retrieve(self.TEST_DATASET_NAME)
        self.assertTrue('id' in dataset,
                        'Should be able to get id in dataset')
        check_fields = set(['class_name', 'created_at',
                            'data_url',
                            'depository', 'depository_id',
                            'depository_version', 'depository_version_id',
                            'description',
                            'fields_url', 'full_name',
                            'genomic_builds', 'is_genomic',
                            'id',
                            'name', 'title', 'updated_at',
                            'url'])
        self.assertSetEqual(set(dataset.keys()), check_fields)

    def test_dataset_fields(self):
        fields = Dataset.retrieve(self.TEST_DATASET_NAME).fields()
        dataset_field = fields.data[0]
        self.assertTrue('id' in dataset_field,
                        'Should be able to get id in list of dataset fields')

        check_fields = set(['class_name', 'created_at',
                            'data_type', 'dataset', 'dataset_id',
                            'description', 'facets_url',
                            'full_name', 'id',
                            'name', 'updated_at',
                            'url'])
        self.assertSetEqual(set(dataset_field.keys()), check_fields)
        expected = """

| Field                        | Data Type   | Description   |
|------------------------------+-------------+---------------|
| accession_numbers            | string      |               |
| approved_name                | string      |               |
| approved_symbol              | string      |               |
| ccds_ids                     | string      |               |
| chromosome                   | string      |               |
| date_approved                | date        |               |
| date_modified                | date        |               |
| date_name_changed            | date        |               |
| date_symbol_changed          | date        |               |
| ensembl_gene_id              | string      |               |
| ensembl_id_ensembl           | string      |               |
| entrez_gene_id               | string      |               |
| entrez_gene_id_ncbi          | string      |               |
| enzyme_ids                   | string      |               |
| gene_family_description      | string      |               |
| gene_family_tag              | string      |               |
| hgnc_id                      | long        |               |
| locus                        | string      |               |
| locus_group                  | string      |               |
| locus_specific_databases     | string      |               |
| locus_type                   | string      |               |
| mouse_genome_database_id     | long        |               |
| mouse_genome_database_id_mgi | long        |               |
| name_synonyms                | string      |               |
| omim_id_ncbi                 | string      |               |
| omim_ids                     | long        |               |
| previous_names               | string      |               |
| previous_symbols             | string      |               |
| pubmed_ids                   | string      |               |
| rat_genome_database_id_rgd   | long        |               |
| record_type                  | string      |               |
| refseq_id_ncbi               | string      |               |
| refseq_ids                   | string      |               |
| specialist_database_id       | string      |               |
| specialist_database_links    | string      |               |
| status                       | string      |               |
| synonyms                     | string      |               |
| ucsc_id_ucsc                 | string      |               |
| uniprot_id_uniprot           | string      |               |
| vega_ids                     | string      |               |
"""
        self.assertEqual("{0}".format(fields), expected[1:-1],
                         'tabulated dataset fields')

    def test_dataset_facets(self):
        field = Dataset.retrieve(self.TEST_DATASET_NAME).fields('hgnc_id')
        facets = field.facets()
        self.assertTrue(facets.total >= 0,
                        'facet should have an total field >= 0')
