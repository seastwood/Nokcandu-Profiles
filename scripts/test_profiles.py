import copy
import unittest
import profiles

class ProfileCompleteness(unittest.TestCase):
    def profile(self):
        return {'schema': 2, 'title': 'BF1942', 'source': 'folder', 'rating': 'works', 'match': {'exeName': 'BF1942.exe'},
                'rawMouse': 1, 'rawMouseFrameSync': True,
                'gameDisplay': {'recipe': 'bf1942', 'resolution': [1280,800], 'menuCorrection': True},
                'performance': {'fpsCounter': True, 'vsync': False, 'fpsLimit': 60, 'lowLatency': True, 'hud': 'graph', 'hudSize': 'small'}}
    def test_new_settings_survive_catalog(self):
        p = self.profile(); clean, errors = profiles.normalize(p)
        self.assertEqual(errors, []); self.assertEqual(clean, p)
    def test_old_profiles_still_supported(self):
        p = self.profile(); p['schema'] = 1; p.pop('gameDisplay'); p.pop('rawMouseFrameSync')
        self.assertEqual(profiles.normalize(p)[1], [])
    def test_new_settings_require_new_schema(self):
        p = self.profile(); p['schema'] = 1
        self.assertTrue(profiles.normalize(p)[1])
    def test_recipe_rejects_untrusted_values_and_wrong_game(self):
        for key, value in [('recipe', 'https://example.com/patch.exe'), ('resolution', [1,2]), ('resolution', [1280.0,800]), ('menuCorrection', 'yes')]:
            p = self.profile(); p['gameDisplay'][key] = value
            self.assertTrue(profiles.normalize(p)[1], (key, value))
        p = self.profile(); p['gameDisplay']['patch'] = 'bytes'
        self.assertTrue(profiles.normalize(p)[1])
        p = self.profile(); p['match']['exeName'] = 'Other.exe'
        self.assertTrue(profiles.normalize(p)[1])
    def test_mouse_and_latency_flags_must_be_boolean(self):
        p = self.profile(); p['rawMouseFrameSync'] = 1
        self.assertTrue(profiles.normalize(p)[1])
        p = self.profile(); p['performance']['lowLatency'] = 'true'
        self.assertTrue(profiles.normalize(p)[1])

if __name__ == '__main__': unittest.main()
