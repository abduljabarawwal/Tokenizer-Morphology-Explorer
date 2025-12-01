import json
import pandas as pd
from typing import List, Dict, Any
import io

class DataExporter:
    def export_to_json(self, results: Any) -> str:
        """
        Complete JSON output.
        """
        # Convert dataclasses to dict if needed, or assume results is dict/list
        def default_serializer(obj):
            if hasattr(obj, '__dict__'):
                return obj.__dict__
            return str(obj)
            
        return json.dumps(results, default=default_serializer, ensure_ascii=False, indent=2)

    def export_to_csv(self, results: Any) -> str:
        """
        CSV format with token details.
        """
        df = self.export_to_dataframe(results)
        return df.to_csv(index=False, encoding='utf-8-sig')

    def export_to_dataframe(self, results: Any) -> pd.DataFrame:
        """
        Pandas DataFrame for further processing.
        """
        # Assuming results has a 'tokens' list
        if hasattr(results, 'tokens'):
            data = [t.__dict__ for t in results.tokens]
        elif isinstance(results, dict) and 'tokens' in results:
            data = results['tokens']
        else:
            data = []
            
        return pd.DataFrame(data)

    def prepare_visualization_data(self, results: Any) -> Dict:
        """
        Format for Plotly charts.
        """
        df = self.export_to_dataframe(results)
        
        if df.empty:
            return {'pos_counts': {}, 'confidence_hist': []}
            
        pos_counts = df['pos_tag'].value_counts().to_dict() if 'pos_tag' in df.columns else {}
        confidence_hist = df['pos_confidence'].tolist() if 'pos_confidence' in df.columns else []
        
        return {
            'pos_counts': pos_counts,
            'confidence_hist': confidence_hist
        }

    def generate_summary_report(self, results: Any) -> str:
        df = self.export_to_dataframe(results)
        return f"Analysis complete. Found {len(df)} tokens."
